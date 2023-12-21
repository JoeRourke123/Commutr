import 'package:commutr/app/components/digest/sections/section_intro.dart';
import 'package:commutr/app/components/digest/sections/spinny_dots_funvas.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:funvas/funvas.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:social_login_buttons/social_login_buttons.dart';
import 'package:widget_and_text_animator/widget_and_text_animator.dart';

class LoginDemo extends SectionIntro {
  LoginDemo(super.width, super.height);

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
            Transform.scale(
              scale: 2.2,
              child: SizedBox(
                  width: width * 4,
                  height: height,
                  child: FunvasContainer(
                    funvas: SpinnyDotsFunvas(),
                  )),
            ),
            Container(
              decoration: BoxDecoration(
                color: Colors.lightBlue.shade800.withOpacity(0.85),
              ),
            ),
            Container(
              margin: EdgeInsets.symmetric(horizontal: 40),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  TextAnimator("Commutr",
                      incomingEffect:
                          WidgetTransitionEffects.incomingSlideInFromLeft(
                              duration: Duration(seconds: 1)),
                      style: GoogleFonts.dmSans(
                        fontWeight: FontWeight.w900,
                        letterSpacing: -2,
                        color: Colors.white,
                        fontSize: 64,
                      )),
                  Container(
                    margin: EdgeInsets.only(bottom: 20),
                    child: WidgetAnimator(
                        incomingEffect:
                            WidgetTransitionEffects.incomingSlideInFromBottom(
                          duration: Duration(seconds: 1),
                          delay: Duration(seconds: 1),
                        ),
                        child: Text(
                          "Log in with",
                          style: GoogleFonts.dmSans(
                              fontSize: 28,
                              color: Colors.white,
                              fontWeight: FontWeight.bold),
                        )),
                  ),
                  WidgetAnimator(
                      incomingEffect:
                          WidgetTransitionEffects.incomingSlideInFromBottom(
                        duration: Duration(seconds: 1),
                        delay: Duration(seconds: 1),
                      ),
                      child: Container(
                        margin: EdgeInsets.only(bottom: 15),
                        child: SocialLoginButton(
                          buttonType: SocialLoginButtonType.apple,
                          onPressed: () {},
                          borderRadius: 40,
                        ),
                      )),
                  WidgetAnimator(
                      incomingEffect:
                          WidgetTransitionEffects.incomingSlideInFromBottom(
                        duration: Duration(seconds: 1),
                        delay: Duration(seconds: 1),
                      ),
                      child: SocialLoginButton(
                        buttonType: SocialLoginButtonType.google,
                        onPressed: () {},
                        borderRadius: 40,
                      ))
                ],
              ),
            )
          ],
        ));
  }
}
