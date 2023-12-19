import 'dart:isolate';
import 'dart:ui';

import 'package:commutr/app/services/articles_service.dart';
import 'package:flutter_downloader/flutter_downloader.dart';
import 'package:get/get.dart';

import '../../../data/article_model.dart';


class ArticleController extends GetxController {
  final Article article;
  var loading = false.obs;
  var path = "".obs;

  final ReceivePort _port = ReceivePort();

  ArticleController(this.article);

  @override
  void onReady() {
    super.onReady();
  }

  @override
  void onClose() {
    IsolateNameServer.removePortNameMapping('downloader_send_port');
    super.onClose();
  }

  @override
  void onInit() async {
    super.onInit();

    IsolateNameServer.registerPortWithName(_port.sendPort, 'downloader_send_port');
    _port.listen((dynamic data) {
      int progress = data[2];

      if (progress == 100) {
        loading(false);
      }
    });

    await FlutterDownloader.registerCallback(downloadCallback, step: 10);

    loadContent();
  }

  @pragma('vm:entry-point')
  static void downloadCallback(String id, int status, int progress) {
    final SendPort? send = IsolateNameServer.lookupPortByName('downloader_send_port');
    send!.send([id, status, progress]);
  }

  void loadContent() async {
    loading(true);

    path(await ArticlesService.getArticleContent(article));
  }
}
