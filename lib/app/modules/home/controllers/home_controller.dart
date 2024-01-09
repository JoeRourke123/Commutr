import 'package:commutr/app/services/articles_service.dart';
import 'package:get/get.dart';

import '../../../data/article_model.dart';

class HomeController extends GetxController {
  final loading = false.obs;
  List<Article> articles = List<Article>.empty().obs;

  @override
  void onInit() {
    super.onInit();

    loadArticles();
  }

  @override
  void onReady() {
    super.onReady();
  }

  @override
  void onClose() {
    super.onClose();
  }

  void loadArticles() async {
    loading(true);

    try {
      loading(true);

      articles = await ArticlesService.getArticles();
    } finally {
      loading(false);
    }
  }
}
