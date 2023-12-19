// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'article_model.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Article _$ArticleFromJson(Map<String, dynamic> json) => Article(
      json['id'] as String?,
      json['headline'] as String?,
      json['subtitle'] as String?,
      json['author'] as String?,
      json['published'] == null
          ? null
          : DateTime.parse(json['published'] as String),
      json['url'] as String?,
      json['image'] as String?,
    );

Map<String, dynamic> _$ArticleToJson(Article instance) => <String, dynamic>{
      'id': instance.id,
      'headline': instance.headline,
      'subtitle': instance.subtitle,
      'author': instance.author,
      'published': instance.published?.toIso8601String(),
      'url': instance.url,
      'image': instance.image,
    };
