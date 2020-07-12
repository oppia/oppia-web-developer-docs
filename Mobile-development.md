The following instructions, adapted by royshouvik@ from the [Chrome DevTools Docs](https://developer.chrome.com/devtools/docs/remote-debugging), explain how to do remote debugging on Android devices using Chrome.

**NOTE**: If you just want to view the website on a mobile device, without full fledged debugging, you can start the server as follows: `python -m scripts.start --disable_host_checking` and connect your mobile device to the same Wi-Fi network as your PC. Then, by going to 'http://<[local-ip-address-of-pc]>:8181' on your mobile will open the dev server on it.

## Remote Debugging on Android with Chrome

The way your web content behaves on mobile can be dramatically different from the desktop experience. Remote debugging with Chrome DevTools lets you debug live content on your Android device from your development machine.

### Debugging Chrome for Android using the Chrome Developer Tools

#### Remote debugging on Android supports:

- Debugging websites in browser tabs.
- Debugging WebViews in native Android apps.
- Screencasting live to your development machine from your Android device.
- Accessing your development server on Android using port forwarding and virtual host mapping.

#### Requirements
We are going to talk about debugging a website in a Chrome browser tab in this document. To begin remote debugging, you need:

1. Chrome 32 or later installed on your development machine.
2. A USB cable to connect your Android device.
3. For browser debugging: Android 4.0+ and Chrome for Android.

**Note:** Remote debugging requires your version of desktop Chrome to be newer than the version of Chrome for Android on your device. For best results, use Chrome Canary (Mac/Windows) or the Chrome Dev channel release (Linux) on desktop and Chrome Stable on Android. This ensures the version of desktop Chrome is newer than the version of Chrome for Android.


#### Setting up your Android device
Follow these instructions to set up your Android device for remote debugging.

##### Enable USB debugging
1. On your Android device, select Settings > Developer options. **Note:** On Android 4.2 and later, the developer options are hidden by default. To enable the developer options, select Settings > About phone and tap Build number seven times.

2. In Developer options, select the USB debugging checkbox:

3. If an alert prompts you to allow USB debugging. Tap OK.

##### Connect your device
1. Connect the Android device to your development machine using a USB cable. **Note:** If you are developing on Windows, install the appropriate USB driver for your device. See OEM USB Drivers on the Android Developers' site.

##### Discovering devices in Chrome
1. After setting up remote debugging on Android, discover your device in Chrome.
2. On your desktop Chrome browser, navigate to chrome://inspect. Confirm that Discover USB devices is checked.
3. On your device, an alert prompts you to allow USB debugging from your computer. Tap OK.
4. The message USB debugging connected displays in the device's notification drawer. **Note:** During remote debugging, Chrome prevents your device’s screen from going to sleep. This feature is useful for debugging, but is also less secure. So be sure to keep an eye on your device!
5. On your computer, the chrome://inspect page displays every connected device, along with its open tabs and debug-enabled WebViews.

##### Debugging remote browser tabs
1. From the chrome://inspect page, you can launch DevTools and debug your remote browser tabs.
2. To start debugging, click inspect below the browser tab you want to debug.
3. A new instance of Chrome DevTools launches on your computer. From this instance, you can interact with the selected browser tab on your device in real time.

For example, you can use DevTools to inspect web page elements on your device:

- When you mouse over an element in the Elements panel, DevTools highlights the element on your device.
- You can also click the Inspect Element inspect element icon icon in DevTools and tap your device screen. DevTools highlights the tapped element in the Elements panel.


### Debugging tips
Here are a few tips to help get you started with remote debugging:

- Use F5 (or Cmd+r on Mac) to reload a remote page from the DevTools window.
- Keep the device on a cellular network. Use the Network panel to view the network waterfall under actual mobile conditions.
- Use the Timeline panel to analyze rendering and CPU usage. Hardware on mobile devices often runs much slower than on your development machine.
- If you’re running a local web server, use port forwarding or virtual host mapping to access the site on your device.

##### Live screencasting
Shifting your attention between screens isn’t always convenient. Screencast displays your device's screen right alongside DevTools on your development machine. You can interact with the content on your device from the screencast too.

As of KitKat 4.4.3, screencast is available for both browser tabs and Android WebViews.

1. To start screencasting, click the Screencast screencast icon icon in the upper right corner of your remote debugging DevTools window.
2. The Screencast panel opens on the left and displays a live view of your device's screen.

Screencast only displays page content. Transparent portions of the screencast are covered by the omnibox, device keyboard, and other device interfaces.

**Note:** Because screencast continuously captures frames, it has some performance overhead. If your tests are sensitive to frame rate, disable screencast.

When you interact with the screencast, clicks are translated into taps, firing proper touch events on the device. Keystrokes from your computer are sent to the device, so you can avoid typing with your thumbs.

Other DevTools work with the screencast too. For example, to inspect an element, click the Inspect Element inspect element icon icon and then click inside the screencast.

*Tips:* To simulate a pinch gesture, hold Shift while dragging. To scroll, use your trackpad or mouse wheel or fling with your pointer.

##### Port forwarding

Port forwarding on Chrome for Android makes it easy to test your development site on mobile. It works by creating a listening TCP port on your mobile device that maps to a particular TCP port on your development machine. Traffic between these ports travels through USB, so the connection doesn't depend on your network configuration.

To enable port forwarding:

1. Open chrome://inspect on your development machine.
2. Click Port Forwarding. The port forwarding settings display.
3. In the Device port field, enter the port number you want your Android device to listen on. 
(The default port is 8080.)
4. In the Host field, enter the IP address (or hostname) and port number where your web application is running. 
5. This address can be any local location accessible from your development machine. Currently, port numbers must be between 1024 and 32767 (inclusive).
6. Check Enable port forwarding.
7. Click Done.
8. The port status indicators on chrome://inspect are green when port forwarding is successful.

Now you can open a new Chrome for Android tab and view the content of your local server on your device.