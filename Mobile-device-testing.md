The following instructions (contributed by @edallison) outline how to test the behavior an Oppia development server on iOS and Android. If you have one of these devices, you should be able to test the development server directly; otherwise, you may have to use the Chrome mobile emulator or install an emulator on your desktop machine. Instructions for all these cases are provided below.

## Accessing an Oppia development instance via a mobile device

1. Ensure that the device hosting your Oppia developer instance, as well as the mobile device you will be testing the instance on, are both connected to the same network.
2. Determine the local IP of the device hosting your Oppia instance:
  * Windows: Open the Command Prompt and enter `ipconfig`.
  * OS X: Open `System Preferences > Network`
  * Linux: In a terminal, enter `ip addr show`.
3. In the browser on your mobile device, enter the local IP address found in the previous step into the browser address bar, followed by `:8181` (e.g. `xxx.xxx.xxx.x:8181`).

A lot of developers have faced an issue "Request Host not whitelisted". To workaround this issue, modify the host parameter [here](https://github.com/oppia/oppia/blob/450e094392995794553b2ad64cd82c233d9b591d/scripts/start.py#L148) from `--host 0.0.0.0` to `--host xxx.xxx.x.xxx` where xxx.xxx.x.xxx is your local IP. After restarting the server, you can access the Oppia instance on your mobile device as mentioned in step 3 above. (Note: If you make a PR after testing using these steps, please remember to revert these changes.)

## Using the Chrome mobile emulator

1. Follow the instructions on this [Google Developers page](https://developers.google.com/web/tools/chrome-devtools/iterate/device-mode/).

## Installing iOS Simulator (for OS X)

1. Install Xcode via the [Mac App Store](https://itunes.apple.com/us/app/xcode/id497799835?mt=12).
1. Right click on the Xcode icon in the dock, then select `Open Developer Tools > Simulator`.
1. Once the simulator app icon appears in the dock, you can either pin it in the dock, or move/copy the app to a more convenient location for future access. This allows you to open the simulator without having to first open Xcode.
1. Open Safari, then navigate to a locally-hosted developer instance to test Oppia on iOS.

## Installing Android Emulator

1. Follow the directions for installing the [Android SDK Tools](https://developer.android.com/sdk/installing/index.html?pkg=tools).
1. Run the SDK manager:
  * Windows: Double-click the `SDK Manager.exe` file at the root of the Android SDK directory.
  * OS X/Linux: Open a terminal and navigate to the `tools/` directory in the location where the Android SDK was installed. Then, execute `android sdk`.
1. Download all packages under a given Android API directory (e.g. Android 6.0), as well as all packages under the Tools directory.
1. Using the command line, navigate to your SDK’s `tools/` directory and execute `android avd`.
1. With Android Virtual Device selected, click the `Create` button.
1. Create a name for the AVD Name field.
1. Select an available device for the Device field.
1. Select an available target API for the Target field.
1. Select an available CPU for the CPU field.
1. Select a skin for the Skin field.
1. Click OK to create an AVD.
1. In AVD Manager, select your AVD, and click Start to boot your virtual device.
