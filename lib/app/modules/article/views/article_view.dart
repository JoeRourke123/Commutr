import 'package:commutr/app/data/article_model.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';

import 'package:get/get.dart';
import 'package:pdf_viewer_plugin/pdf_viewer_plugin.dart';

import '../controllers/article_controller.dart';

class ArticleView extends GetView<ArticleController> {

  const ArticleView({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return CupertinoPageScaffold(
      child: Padding(
        padding: EdgeInsets.symmetric(horizontal: 20, vertical: 20),
        child: Container(
          width: MediaQuery.of(context).size.width,
          height: MediaQuery.of(context).size.height,
          alignment: Alignment.center,
          child: controller.loading.value && controller.path.isNotEmpty ? SpinKitFadingCircle(
            color: CupertinoColors.systemPurple,
          ) : PdfView(path: controller.path.value),
        ),
      )
    );
  }
}
