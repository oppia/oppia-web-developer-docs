If you need to debug the data in Google Cloud Datastore Emulator when running the devserver on localhost (e.g. you want to look what models are in the datastore emulator or you want to add or modify them) you cannot use the admin environment provided by the devserver as it cannot access the datastore emulator anymore (since Python 3 introduction). You need to use some custom GUI for the emulator, [DSAdmin](https://github.com/remko/dsadmin) is probably one of the best ones.

## How to use DSAdmin

1. Download an archive for your platform and processor from the [DSAdmin releases GitHub page](https://github.com/remko/dsadmin/releases)
2. Unpack the archive and put the binary somewhere you can easily access it through the terminal
3. Run the devserver
4. While the devserver is running run `<path to DSAdmin binary> --project=dev-project-id --datastore-emulator-host=localhost:8089` in a different terminal window or tab (for example if you put the DSAdmin into the parent folder of oppia, you can run it like this `../dsadmin  --project=dev-project-id --datastore-emulator-host=localhost:8089`
5. You will see an output saying something like `<date> <time> dsadmin (project 'dev-project-id') listening on <URL>` then you can navigate to the URL and you will see the UI
