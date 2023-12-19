class CommutrUrls {
  static final baseUrl = Uri.parse("http://localhost:8000/api/");
  static final articlesUrl = Uri.parse( "${baseUrl}articles/");
  static Uri articleContentUrl(String articleId) => Uri.parse("${baseUrl}article/$articleId/");
}