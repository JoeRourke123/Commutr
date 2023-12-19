import 'package:flutter/cupertino.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';

import 'package:get/get.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:super_cupertino_navigation_bar/super_cupertino_navigation_bar.dart';

import '../../../components/article_card.dart';
import '../controllers/home_controller.dart';

class HomeView extends GetView<HomeController> {
  const HomeView({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return CupertinoPageScaffold(
        child: SuperCupertinoNavigationBar(
            automaticallyImplyLeading: false,
            largeTitle: Text("Commutr",
                style: GoogleFonts.cabin(
                    fontWeight: FontWeight.bold, fontStyle: FontStyle.italic)),
            appBarType: AppBarType.LargeTitleWithPinnedSearch,
            previousPageTitle: "Widgets",
            padding: EdgeInsetsDirectional.symmetric(vertical: 20),
            stretch: true,
            avatarModel: AvatarModel(
              avatarIsVisible: true,
              onTap: null,
              avatarIconColor: CupertinoColors.systemPurple,
              icon: CupertinoIcons.profile_circled,
            ),
            slivers: [
          SliverToBoxAdapter(
            child: Padding(
              padding: const EdgeInsets.only(
                  left: 15.0, right: 15.0, top: 10.0, bottom: 15),
              child: Text(
                "Your Articles",
                style: TextStyle(
                  fontSize: 20,
                  fontWeight: FontWeight.w700,
                ),
              ),
            ),
          ),
          SliverPadding(
            padding: EdgeInsets.symmetric(horizontal: 20),
            sliver: controller.loading.value
                ? SliverFillRemaining(
                    hasScrollBody: false,
                    child: Center(
                      child: SpinKitFadingCircle(
                        color: CupertinoColors.systemPurple,
                      ),
                    ))
                : SliverAnimatedList(
                    itemBuilder: (context, articleIndex, _b) {
                      final article = controller.articles[articleIndex];
                      return ArticleCard(
                        article: article,
                      );
                    },
                    initialItemCount: controller.articles.length,
                  ),
          )
        ]));
  }
}
