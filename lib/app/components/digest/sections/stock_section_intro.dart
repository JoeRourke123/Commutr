import 'package:commutr/app/components/digest/sections/section_intro.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:funvas/funvas.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:widget_and_text_animator/widget_and_text_animator.dart';

import '../../funvas/arrows_funvas.dart';

class StockSectionIntro extends SectionIntro {
  StockSectionIntro(super.width, super.height);

  @override
  Widget build(BuildContext context) {
    return Container(
        width: width,
        decoration: BoxDecoration(
          color: CupertinoColors.darkBackgroundGray,
        ),
        child: Stack(
          alignment: Alignment.topCenter,
          children: [
            SizedBox(
                width: width,
                height: height,
                child: FunvasContainer(
                  funvas: ArrowsFunvas(),
                )),
            Container(
              width: width,
              height: height,
              decoration: BoxDecoration(
                color: Colors.black.withOpacity(0.75),
              ),
            ),
            SafeArea(
                child: Column(
              children: [
                WidgetAnimator(
                  incomingEffect:
                      WidgetTransitionEffects.incomingOffsetThenScale(
                          duration: Duration(seconds: 1)),
                  child: Text("Stocks",
                      style: GoogleFonts.montserrat(
                        fontWeight: FontWeight.w800,
                        color: Colors.white,
                        fontSize: 72,
                      )),
                ),
                Expanded(
                    child: WidgetAnimator(
                  incomingEffect:
                      WidgetTransitionEffects.incomingSlideInFromBottom(
                          delay: Duration(seconds: 1),
                          duration: Duration(milliseconds: 1000)),
                  child: Container(
                      decoration: BoxDecoration(
                          color: Colors.white.withOpacity(0.85),
                          boxShadow: [BoxShadow(color: Colors.white54, offset: Offset(0, 3), blurRadius: 8, spreadRadius: 2)],
                          borderRadius: BorderRadius.circular(30)),
                      margin:
                          EdgeInsets.symmetric(horizontal: 40, vertical: 20),
                      padding: EdgeInsets.all(30),
                      child: Column(
                        children: [
                          Container(
                            child: Row(
                              mainAxisSize: MainAxisSize.max,
                              mainAxisAlignment: MainAxisAlignment.spaceBetween,
                              crossAxisAlignment: CrossAxisAlignment.center,
                              children: [
                                Column(
                                  mainAxisAlignment: MainAxisAlignment.start,
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Text(
                                      "EXPE",
                                      style: GoogleFonts.dmSans(
                                          fontSize: 42,
                                          color: Colors.black,
                                          fontWeight: FontWeight.w900),
                                    ),
                                    Text(
                                      "+3.24",
                                      style: GoogleFonts.dmMono(
                                          fontSize: 18,
                                          color: Colors.green.shade700,
                                          fontWeight: FontWeight.bold),
                                    ),
                                  ],
                                ),
                                Column(
                                  mainAxisAlignment: MainAxisAlignment.start,
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Text(
                                      "\$151.52",
                                      style: GoogleFonts.dmMono(
                                          fontSize: 24,
                                          color: Colors.black87,
                                          fontWeight: FontWeight.w900),
                                    ),
                                  ],
                                ),
                              ],
                            ),
                            padding: EdgeInsets.only(bottom: 10),
                            margin: EdgeInsets.only(bottom: 20),
                          ),
                          Container(
                            child: Row(
                              mainAxisSize: MainAxisSize.max,
                              mainAxisAlignment: MainAxisAlignment.spaceBetween,
                              crossAxisAlignment: CrossAxisAlignment.center,
                              children: [
                                Column(
                                  mainAxisAlignment: MainAxisAlignment.start,
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Text(
                                      "APPL",
                                      style: GoogleFonts.dmSans(
                                          fontSize: 42,
                                          color: Colors.black,
                                          fontWeight: FontWeight.w900),
                                    ),
                                    Text(
                                      "+1.44",
                                      style: GoogleFonts.dmMono(
                                          fontSize: 18,
                                          color: Colors.green.shade700,
                                          fontWeight: FontWeight.bold),
                                    ),
                                  ],
                                ),
                                Column(
                                  mainAxisAlignment: MainAxisAlignment.start,
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Text(
                                      "\$196.94",
                                      style: GoogleFonts.dmMono(
                                          fontSize: 24,
                                          color: Colors.black87,
                                          fontWeight: FontWeight.w900),
                                    ),
                                  ],
                                ),
                              ],
                            ),
                            padding: EdgeInsets.only(bottom: 10),
                            margin: EdgeInsets.only(bottom: 20),
                          ),
                          Container(
                            child: Row(
                              mainAxisSize: MainAxisSize.max,
                              mainAxisAlignment: MainAxisAlignment.spaceBetween,
                              crossAxisAlignment: CrossAxisAlignment.center,
                              children: [
                                Column(
                                  mainAxisAlignment: MainAxisAlignment.start,
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Text(
                                      "TSLA",
                                      style: GoogleFonts.dmSans(
                                          fontSize: 42,
                                          color: Colors.black,
                                          fontWeight: FontWeight.w900),
                                    ),
                                    Text(
                                      "-\$0.97",
                                      style: GoogleFonts.dmMono(
                                          fontSize: 18,
                                          color: Colors.red.shade700,
                                          fontWeight: FontWeight.bold),
                                    ),
                                  ],
                                ),
                                Column(
                                  mainAxisAlignment: MainAxisAlignment.start,
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Text(
                                      "\$257.22",
                                      style: GoogleFonts.dmMono(
                                          fontSize: 24,
                                          color: Colors.black87,
                                          fontWeight: FontWeight.w900),
                                    ),
                                  ],
                                ),
                              ],
                            ),
                            padding: EdgeInsets.only(bottom: 10),
                            margin: EdgeInsets.only(bottom: 20),
                          )
                        ],
                      )),
                )),
              ],
            ))
          ],
        ));
  }
}
