import 'package:commutr/app/data/article_model.dart';
import 'package:commutr/app/modules/article/views/article_view.dart';
import 'package:cupertino_rounded_corners/cupertino_rounded_corners.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter_gradients_reborn/flutter_gradients_reborn.dart';
import 'package:get/get.dart';

class ArticleCard extends StatelessWidget {
  final Article article;

  const ArticleCard({super.key, required this.article});

  @override
  Widget build(BuildContext context) {
    return CupertinoCard(
      splashColor: CupertinoColors.systemPink.withAlpha(32),
      child: Container(
        constraints: BoxConstraints.expand(
          height: 256
        ),
        alignment: Alignment.bottomLeft,
        child: Padding(
          padding: EdgeInsets.all(32.0),
          child: Text(
            article.headline!,
            style: TextStyle(color: CupertinoColors.white, fontSize: 28, fontWeight: FontWeight.bold),
          ),
        ),
      ),
      decoration: BoxDecoration(
        gradient: FlutterGradients.ripeMalinka(tileMode: TileMode.mirror)
      ),
      elevation: 2.0,
      margin: const EdgeInsets.all(8.0),
      padding: const EdgeInsets.all(10.0),
      radius: BorderRadius.all(
        new Radius.circular(40.0),
      ),
      onPressed: () {
        Get.toNamed(
          "/article",
          arguments: article
        );
      },
    );
  }

}