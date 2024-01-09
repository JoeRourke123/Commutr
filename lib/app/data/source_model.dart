import 'package:json_annotation/json_annotation.dart';

part 'source_model.g.dart';

@JsonSerializable()
class Source {
  String? id;
  String? name;
  List<String>? topics;

  Source({this.id, this.name, this.topics});

  factory Source.fomJson(Map<String,dynamic> json) => _$SourceFromJson(json);

  Map<String, dynamic> toJson() => _$SourceToJson(this);
}