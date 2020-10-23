Please use the following process for launching major new features that lead to a user-visible change:

- Before doing anything else, please:
    - Make sure e2e tests are present for your feature.
    - Make sure it is easy to toggle on and off, in case it needs to be aborted for the release. This implies proper gating of views, controllers, etc.
- Fill out this [google form](https://forms.gle/m2u1VkQDXWee4euAA).
- Nithesh (**@nithusha21**) will first do a quick audit of the feature, in order to ensure that it is ready for testing. If the feature is not ready, he will get back to you with what needs to be done, and abort the launch. If the feature passes initial checks, he will put you in touch with a product tester. (The expected turnaround time for this part is < 48 hours.)
- The new feature will then be deployed to a custom server, and Nithesh will let the product tester know when the feature is ready for testing. The tester will be given 1 week to file any issues they find.
- Any bugs found will need to be fixed before the target release. (Preferably before the release cut, but if it doesn't make it, then all the issues will be considered blockers for the release).
- If the major bugs aren't fixed by the time of the release, then you will need to toggle the feature off, and cherrypick that PR for the release.
- (Optional) If you like, you can fill in [this form](https://goo.gl/forms/sNBWrW03fS6dBWEp1) to announce your feature to the public once it's launched!
