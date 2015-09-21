library hauberk.content.maze_dungeon;

import 'dart:math' as math;

import 'package:piecemeal/piecemeal.dart';

import '../engine.dart';
import 'stage_builder.dart';
import 'tiles.dart';

abstract class Dungeon extends StageBuilder {
  int get numRoomTries;

  int get extraConnectorChance => 20;

  int get roomExtraSize => 0;

  int get windingPercent => 0;

  var _rooms = <Rect>[];

  Array2D<int> _regions;

  int _currentRegion = -1;

  void generate(Stage stage) {
    if (stage.width % 2 == 0 || stage.height % 2 == 0) {
      throw new ArgumentError("The stage must be odd-sized.");
    }

    bindStage(stage);

    fill(Tiles.wall);
    _regions = new Array2D(stage.width, stage.height);

    _addRooms();

    for (var y = 1; y < bounds.height; y += 2) {
      for (var x = 1; x < bounds.width; x += 2) {
        var pos = new Vec(x, y);
        if (getTile(pos) != Tiles.wall) continue;
        _growMaze(pos);
      }
    }

    _connectRegions();
    _removeDeadEnds();

    _rooms.forEach(onDecorateRoom);
  }

  void onDecorateRoom(Rect room) {}

  void _growMaze(Vec start) {
    var cells = <Vec>[];
    var lastDir;

    _startRegion();
    _carve(start);

    cells.add(start);
    while (cells.isNotEmpty) {
      var cell = cells.last;

      var unmadeCells = <Direction>[];

      for (var dir in Direction.CARDINAL) {
        if (_canCarve(cell, dir)) unmadeCells.add(dir);
      }

      if (unmadeCells.isNotEmpty) {
        var dir;
        if (unmadeCells.contains(lastDir) && rng.range(100) > windingPercent) {
          dir = lastDir;
        } else {
          dir = rng.item(unmadeCells);
        }

        _carve(cell + dir);
        _carve(cell + dir * 2);

        cells.add(cell + dir * 2);
        lastDir = dir;
      } else {
        cells.removeLast();
        lastDir = null;
      }
    }
  }

  void _addRooms() {
    for (var i = 0; i < numRoomTries; i++) {
      var size = rng.range(1, 3 + roomExtraSize) * 2 + 1;
      var rectangularity = rng.range(0, 1 + size ~/ 2) * 2;
      var width = size;
      var height = size;
      if (rng.oneIn(2)) {
        width += rectangularity;
      } else {
        height += rectangularity;
      }

      var x = rng.range((bounds.width - width) ~/ 2) * 2 + 1;
      var y = rng.range((bounds.height - height) ~/ 2) * 2 + 1;

      var room = new Rect(x, y, width, height);

      var overlaps = false;
      for (var other in _rooms) {
        if (room.distanceTo(other) <= 0) {
          overlaps = true;
          break;
        }
      }

      if (overlaps) continue;

      _rooms.add(room);

      _startRegion();
      for (var pos in new Rect(x, y, width, height)) {
        _carve(pos);
      }
    }
  }

  void _connectRegions() {
    // Find all of the tiles that can connect two (or more) regions.
    var connectorRegions = <Vec, Set<int>>{};
    for (var pos in bounds.inflate(-1)) {
      // Can't already be part of a region.
      if (getTile(pos) != Tiles.wall) continue;

      var regions = new Set<int>();
      for (var dir in Direction.CARDINAL) {
        var region = _regions[pos + dir];
        if (region != null) regions.add(region);
      }

      if (regions.length < 2) continue;

      connectorRegions[pos] = regions;
    }

    var connectors = connectorRegions.keys.toList();

    var merged = {};
    var openRegions = new Set<int>();
    for (var i = 0; i <= _currentRegion; i++) {
      merged[i] = i;
      openRegions.add(i);
    }
    while (openRegions.length > 1) {
      var connector = rng.item(connectors);

      // Carve the connection.
      _addJunction(connector);

      var regions = connectorRegions[connector]
          .map((region) => merged[region]);
      var dest = regions.first;
      var sources = regions.skip(1).toList();

      for (var i = 0; i <= _currentRegion; i++) {
        if (sources.contains(merged[i])) {
          merged[i] = dest;
        }
      }

      openRegions.removeAll(sources);
      connectors.removeWhere((pos) {
        if (connector - pos < 2) return true;

        var regions = connectorRegions[pos].map((region) => merged[region])
            .toSet();

        if (regions.length > 1) return false;

        if (rng.oneIn(extraConnectorChance)) _addJunction(pos);

        return true;
      });
    }
  }

  void _addJunction(Vec pos) {
    if (rng.oneIn(4)) {
      setTile(pos, rng.oneIn(3) ? Tiles.openDoor : Tiles.floor);
    } else {
      setTile(pos, Tiles.closedDoor);
    }
  }

  void _removeDeadEnds() {
    var done = false;

    while (!done) {
      done = true;

      for (var pos in bounds.inflate(-1)) {
        if (getTile(pos) == Tiles.wall) continue;

        // If it only has one exit, it's a dead end.
        var exits = 0;
        for (var dir in Direction.CARDINAL) {
          if (getTile(pos + dir) != Tiles.wall) exits++;
        }

        if (exits != 1) continue;

        done = false;
        setTile(pos, Tiles.wall);
      }
    }
  }
  bool _canCarve(Vec pos, Direction direction) {
    // Must end in bounds.
    if (!bounds.contains(pos + direction * 3)) return false;

    // Destination must not be open.
    return getTile(pos + direction * 2) == Tiles.wall;
  }

  void _startRegion() {
    _currentRegion++;
  }

  void _carve(Vec pos, [TileType type]) {
    if (type == null) type = Tiles.floor;
    setTile(pos, type);
    _regions[pos] = _currentRegion;
  }
}
