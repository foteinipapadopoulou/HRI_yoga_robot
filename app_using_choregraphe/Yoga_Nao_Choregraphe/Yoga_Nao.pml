<?xml version="1.0" encoding="UTF-8" ?>
<Package name="Yoga_Nao" format_version="5">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_with_feedback" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="try_new_poses" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="ReturnToInitialPosition/behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs />
    <Resources>
        <File name="icon" src="icon.png" />
        <File name="server_config" src="behavior_with_feedback/server_config.txt" />
        <File name="camera1" src="behavior_with_feedback/camera1.ogg" />
        <File name="image" src="behavior_without_feedback/image.png" />
        <File name="manifest" src="ReturnToInitialPosition/manifest.xml" />
        <File name="ReturnToInitialPosition" src="ReturnToInitialPosition/ReturnToInitialPosition.pml" />
        <File name="behavior_2" src="try_new_poses/behavior_2.xar" />
    </Resources>
    <Topics />
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
