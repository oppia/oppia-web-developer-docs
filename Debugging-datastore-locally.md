If you need to debug the data in Google Cloud Datastore Emulator when running the devserver on localhost (e.g. you want to look what models are in the datastore emulator or you want to add or modify them) you cannot use the admin environment provided by the devserver as it cannot access the datastore emulator anymore (since Python 3 introduction). You need to use some custom GUI for the emulator, [DSAdmin](https://github.com/remko/dsadmin) is probably one of the best ones.

## How to clear local datastore data

In some cases it is possible that the local datastore data are not deleted when the server is rerun, you can delete the data by running `curl -X POST http://localhost:8089/reset` when the devserver is running.

## How to start DSAdmin

# Docker Setup

1. Build and run dev-server using `make build` and `make run-devserver` respectively.
2. Once the dev-server is running, run `make run-dsadmin` in a separate terminal window.
3. Navigate to `localhost:8080` to access DSAdmin.

## Python Setup

1. Download an archive for your platform and processor from the [DSAdmin releases GitHub page](https://github.com/remko/dsadmin/releases)
2. Unpack the archive and put the binary somewhere you can easily access it through the terminal
3. Run the devserver
4. While the devserver is running run `<path to DSAdmin binary> --project=dev-project-id --datastore-emulator-host=localhost:8089` in a different terminal window or tab (for example if you put the DSAdmin into the parent folder of oppia, you can run it like this `../dsadmin  --project=dev-project-id --datastore-emulator-host=localhost:8089`
5. You will see an output saying something like `<date> <time> dsadmin (project 'dev-project-id') listening on <URL>` then you can navigate to the URL and you will see the UI

## How to use DSAdmin

The UI of the DSAdmin should be fairly self-explanatory, here are some screenshots that can help you get started.

### Empty datastore without any data

This is a screenshot of accessing the DSAdmin when there are no data in the datastore.

[[images/DSAdmin/empty.png|empty datastore]]

### Datastore with some data

This is a screenshot of DSAdmin with some data in the datastore. You can filter different kinds of models, you can sort the models according to some properties. By clicking the model ID you can edit that model. By clicking the "+" in the top-right corner you can create a new model.

[[images/DSAdmin/data.png|datastore with data]]

### Edit screen of a specific model

This is a screenshot of the model edit screen, you can edit all properties there.

[[images/DSAdmin/edit.png|editing of one model]]

Some properties are decoded, when you want to see the encoded value, you need to click the "{}" button.

[[images/DSAdmin/dictionary.png|button to encode property]]
[[images/DSAdmin/encoded.png|encoded property]]

