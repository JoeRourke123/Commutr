import 'package:commutr/app/components/digest/sections/section_intro.dart';
import 'package:commutr/app/components/funvas/inward_wavy_funvas.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:funvas/funvas.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:widget_and_text_animator/widget_and_text_animator.dart';

class HoroscopeSectionIntro extends SectionIntro {
  HoroscopeSectionIntro(super.width, super.height);

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
          alignment: Alignment.bottomCenter,
          children: [
            Transform.scale(
              scale: 2.0,
              child: SizedBox(
                  width: width * 4,
                  height: height,
                  child: FunvasContainer(
                    funvas: InwardWavyFunvas(),
                  )),
            ),
            Container(
              decoration: BoxDecoration(
                color: Colors.brown.shade900.withOpacity(0.9),
              ),
            ),
            SafeArea(
                child: Column(
              children: [
                Expanded(child: WidgetAnimator(
                  incomingEffect: WidgetTransitionEffects.incomingSlideInFromBottom(
                    delay: Duration(seconds: 1),
                    duration: Duration(milliseconds: 1000)
                  ),
                  child: Container(
                      decoration: BoxDecoration(
                          color: Colors.black.withOpacity(0.6),
                          borderRadius: BorderRadius.circular(30)
                      ),
                      margin: EdgeInsets.symmetric(horizontal: 40, vertical: 20),
                      padding: EdgeInsets.all(30),
                      child: Column(
                        children: [
                          Row(
                            mainAxisSize: MainAxisSize.max,
                            children: [
                              Text("☀️   Leo", style: GoogleFonts.dmSans(
                                  fontSize: 24,
                                  color: Colors.white,
                                  fontWeight: FontWeight.bold
                              ),)
                            ],
                          ),
                          Row(
                            mainAxisSize: MainAxisSize.max,
                            children: [
                              Text("born 22nd August 2001", style: GoogleFonts.dmSans(
                                  fontSize: 18,
                                  color: Colors.white54,
                                  fontWeight: FontWeight.w200
                              ),)
                            ],
                          ),
                          Padding(padding: EdgeInsets.only(top: 10), child: Row(
                              mainAxisSize: MainAxisSize.max,
                              children: [
                                Expanded(child: Text("Your romantic life is packed with fun today while professional success is your companion. Financially you are good and health is also not a concern today.", style: GoogleFonts.dmSerifDisplay(
                                    color: Colors.white,
                                    fontSize: 32
                                ),))
                              ]
                          ),)
                        ],
                      )
                  ),
                )),
                TextAnimator("Horoscope",
                    incomingEffect: WidgetTransitionEffects.outgoingScaleDown(
                        duration: Duration(seconds: 1)),
                    style: GoogleFonts.dmSerifDisplay(
                      fontWeight: FontWeight.w800,
                      color: Colors.white,
                      fontSize: 64,
                    ))
              ],
            ))
          ],
        ));
  }
}
