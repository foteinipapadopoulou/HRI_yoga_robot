<?xml version="1.0" encoding="UTF-8" ?>
<Package name="Yoga_Nao" format_version="5">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_with_feedback" xar="behavior.xar" />
<<<<<<< HEAD
        <BehaviorDescription name="behavior" src="behavior_without_feedback" xar="behavior.xar" />
=======
>>>>>>> ef481a5306a4d99f01a528b51b7405f7eb68c1b8
        <BehaviorDescription name="behavior" src="try_new_poses" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs />
    <Resources>
        <File name="icon" src="icon.png" />
        <File name="server_config" src="behavior_with_feedback/server_config.txt" />
        <File name="camera1" src="behavior_with_feedback/camera1.ogg" />
        <File name="image" src="behavior_without_feedback/image.png" />
    </Resources>
    <Topics />
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
