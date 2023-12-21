import 'package:commutr/app/components/digest/sections/section_intro.dart';
import 'package:commutr/app/components/funvas/sound_bar_funvas.dart';
import 'package:commutr/app/components/funvas/wavy_wheel_funvas.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:funvas/funvas.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:widget_and_text_animator/widget_and_text_animator.dart';

class PlaylistSectionIntro extends SectionIntro {
  PlaylistSectionIntro(super.width, super.height);

  @override
  Widget build(BuildContext context) {
    return Container(
        width: width,
        height: height,
        clipBehavior: Clip.hardEdge,
        decoration: BoxDecoration(
          color: Colors.brown,
        ),
        child: Stack(
          alignment: Alignment.center,
          children: [
            SizedBox(
                width: width,
                height: height,
                child: FunvasContainer(
                  funvas: SoundBarFunvas(),
                )),
            Container(
              decoration: BoxDecoration(
                color: Colors.green.shade800.withOpacity(0.75),
              ),
            ),
            WidgetAnimator(
              child: Opacity(
                opacity: 0.5,
                child: Image.asset("assets/images/record.png", scale: 0.05,),
              ),
              atRestEffect: WidgetRestingEffects.rotate(curve: Curves.linear),
              incomingEffect: WidgetTransitionEffects.incomingScaleUp(delay: Duration(milliseconds: 1200), duration: Duration(seconds: 1)),
            ),
            SizedBox(
              width: width / 1.5,
              child: TextAnimator("Set The Mood",
                  incomingEffect: WidgetTransitionEffects.incomingSlideInFromLeft(
                      duration: Duration(seconds: 1)),
                  style: GoogleFonts.abrilFatface(
                    fontWeight: FontWeight.w800,
                    color: Colors.white,
                    fontSize: 64,
                  )),
            ),
          ],
        ));
  }
}
