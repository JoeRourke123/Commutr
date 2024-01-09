import 'package:commutr/app/data/source_model.dart';
import 'package:json_annotation/json_annotation.dart';

part 'article_model.g.dart';

@JsonSerializable()
class Article {
  String? id;
  String? headline;
  String? subtitle;
  String? author;
  DateTime? published;
  // Source? source;
  String? url;
  String? image;

  Article(this.id, this.headline, this.subtitle, this.author, this.published,
      // this.source,
      this.url, this.image);


  factory Article.fomJson(Map<String,dynamic> json) => _$ArticleFromJson(json);

  Map<String, dynamic> toJson() => _$ArticleToJson(this);
}