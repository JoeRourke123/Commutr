import 'package:carousel_slider/carousel_options.dart';
import 'package:carousel_slider/carousel_slider.dart';
import 'package:commutr/app/components/digest/sections/horoscope_section_intro.dart';
import 'package:commutr/app/components/digest/sections/login_demo.dart';
import 'package:commutr/app/components/digest/sections/playlist_section_intro.dart';
import 'package:commutr/app/components/digest/sections/stock_section_intro.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:funvas/funvas.dart';

import 'package:get/get.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:widget_and_text_animator/widget_and_text_animator.dart';

import '../../../components/funvas/arrows_funvas.dart';
import '../controllers/home_controller.dart';

class HomeView extends GetView<HomeController> {
  const HomeView({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Builder(
        builder: (context) {
          final double height = MediaQuery
              .of(context)
              .size
              .height;
          final double width = MediaQuery
              .of(context)
              .size
              .width;
          return Stack(
            alignment: Alignment.bottomLeft,
            children: [
              CarouselSlider(
                  options: CarouselOptions(
                    height: height,
                    viewportFraction: 1.0,
                    enlargeCenterPage: false,
                    autoPlay: false,
                    onPageChanged: (pageIndex, _) => {
                      controller.pageIndex(pageIndex)
                    }
                  ),
                  items: [
                    StockSectionIntro(width, height),
                    HoroscopeSectionIntro(width, height),
                    PlaylistSectionIntro(width, height),
                    LoginDemo(width, height)
                  ]),
              Container(
                width: width,
                height: 22,
                decoration: BoxDecoration(
                  color: Colors.black.withOpacity(0.5)
                ),
              ),
              Obx(() => AnimatedContainer(
                // Use the properties stored in the State class.
                width: width * ((controller.pageIndex.value + 1) / 4),
                height: 22,
                decoration: BoxDecoration(
                  color: [
                    Colors.white38,
                    Colors.brown.shade300,
                    Colors.green.shade300,
                    Colors.lightBlue.shade300
                  ][controller.pageIndex.value],
                ),
                // Define how long the animation should take.
                duration: const Duration(seconds: 1),
                // Provide an optional curve to make the animation feel smoother.
                curve: Curves.fastOutSlowIn,
              ))
            ],
          );
        },
      ),
    );
  }
}
