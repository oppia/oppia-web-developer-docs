### setup.sh  
Calls gulp.js for its `build` task which builds files for third_party/

### start.sh
Sources setup.sh and then when starting a server calls gulp.js for the `start_devserver` task which has the `build` task as a dependency.