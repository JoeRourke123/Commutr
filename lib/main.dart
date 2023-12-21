import 'package:commutr/app/util/background_article_fetch.dart';
import 'package:commutr/app/util/constants.dart';
import 'package:flutter/material.dart';
import 'package:flutter_downloader/flutter_downloader.dart';
import 'package:workmanager/workmanager.dart';

import 'package:get/get.dart';

import 'app/routes/app_pages.dart';

@pragma('vm:entry-point')
void callbackDispatcher() {
  Workmanager().executeTask((task, inputData) {
    // switch(task) {
    //   case ARTICLE_DIGEST_BG_JOB:
    //     fetchArticleDigest();
    //     break;
    // };

    return Future.value(true);
  });
}

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // await FlutterDownloader.initialize(
  //   debug: true, // optional: set to false to disable printing logs to console (default: true)
  //   ignoreSsl: true // option: set to false to disable working with http links (default: false)
  // );
  //
  // await Workmanager().initialize(
  //   callbackDispatcher, // The top level function, aka callbackDispatcher
  //   isInDebugMode: true // If enabled it will post a notification whenever the task is running. Handy for debugging tasks
  // );
  //
  // Workmanager().registerPeriodicTask("articleDigestFetch", ARTICLE_DIGEST_BG_JOB,
  //   frequency: const Duration(hours: 24),
  //   constraints: Constraints(
  //       networkType: NetworkType.connected,
  //       requiresBatteryNotLow: false,
  //       requiresCharging: false,
  //       requiresStorageNotLow: true
  //   )
  // );

  runApp(
    GetMaterialApp(
      title: "Commutr",
      initialRoute: AppPages.INITIAL,
      getPages: AppPages.routes,
    ),
  );
}
