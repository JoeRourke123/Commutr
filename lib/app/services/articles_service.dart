import 'dart:convert';

import 'package:commutr/app/util/urls.dart';
import 'package:flutter_downloader/flutter_downloader.dart';
import 'package:path_provider/path_provider.dart';

import '../data/article_model.dart';

import 'package:http/http.dart';

class ArticlesService {
  static var client = Client();

  static Future<List<Article>> getArticles() async {
    final articlesRequest = await client.get(CommutrUrls.articlesUrl);
    List<dynamic> articlesResponse = json.decode(utf8.decode(articlesRequest.bodyBytes));

    return articlesResponse.map((article) => Article.fomJson(article)).toList();
  }

  static Future<String> getArticleContent(Article article) async {
    final pdfPath = (await getApplicationDocumentsDirectory()).path;
    final fileName = "${article.id!}.pdf";

    await FlutterDownloader.enqueue(
      url: CommutrUrls.articleContentUrl(article.id!).path,
      headers: {}, // optional: header send with url (auth token etc)
      savedDir: pdfPath,
      fileName: fileName,
      showNotification: true, // show download progress in status bar (for Android)
      openFileFromNotification: true, // click on notification to open downloaded file (for Android)
    );

    return "$pdfPath/$fileName";
  }
}