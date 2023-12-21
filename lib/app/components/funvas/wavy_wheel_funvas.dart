import 'dart:math';

import 'package:flutter/material.dart';
import 'package:funvas/funvas.dart';

class WavyWheelFunvas extends Funvas {
  @override
  void u(double t) {
    t /= 2;
    t *= pi / 2;
    c.drawColor(const Color(0xff000000), BlendMode.srcOver);
    const d = 750.0, r = d / 2.1;
    s2q(d);
    c.translate(d / 2, d / 2);
    const n = 5;
    for (var i = 0; i < n; i++) {
      _drawWheel(t + 2 * pi / n * i, r);
    }
  }

  void _drawWheel(double t, double r) {
    c.save();
    const n = 42;
    for (var i = 0; i < n; i++) {
      c.rotate(2 * pi / n);
    }
    c.restore();
  }
}