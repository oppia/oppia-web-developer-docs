Procedure to apply for launching new features:

- Things to check before filling out the form:
    - Make sure e2e tests are present for your feature.
    - Make sure it is easy to toggle on and off, in case it needs to be aborted for the release. This implies proper gating of views, controllers, etc.
- Fill out this [google form](https://forms.gle/m2u1VkQDXWee4euAA).
- Nithesh will first do a quick audit of the feature to ensure it is ready for testing. If not ready, revert back to the project lead with what needs to be done, and abort the launch. Nithesh will get back to you within 48 hours, along with a product tester.
- We would deploy to a custom server, and let you know when it is ready for testing.
- The tester will be given 1 week to file any issues they find.
- The bugs will need to be fixed before the target release. (Preferably before the release cut, but if it doesn’t make it, then all the issues will be considered blockers for the release).
- If the major bugs aren't fixed by the time of the release, you'll need to toggle the feature off, and cherrypick that PR for the release.
- (Optional) If you like, you can fill in [this form](https://goo.gl/forms/sNBWrW03fS6dBWEp1) to announce your feature to the public!
