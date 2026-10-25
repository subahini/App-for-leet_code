# ArrayStep

By **Subahini Nadarajh**. Version 0.1.0, private release preparation.

A self-study app with 56 units in eight paths: Python, arrays and algorithms, data structures, math, machine learning, AI engineering, software engineering, and interview/exam practice. Each path has a searchable problem list, original explanations, Python examples, practice tasks, recall quizzes, notes, local progress and XP.

## Run and build

Requirements: Node 22+, Python 3 for the content check. No API key or AI subscription is needed.

```sh
npm ci
npm run check
python3 -m http.server 8000 --directory dist
```

Open http://localhost:8000. `dist/` is the canonical browser app. It is tracked source, not generated build output. The Python editor saves drafts; it does **not** execute Python.

```sh
npm run sync
npm run android
npm run ios
```

Capacitor projects are in `android/` and `ios/`. Native assets are generated from `dist/` into ignored `mobile-web/` by `npm run build`. The native bridge opens optional external exercises in a system browser and exports backups using the OS share sheet. Lessons work from bundled assets without login or a server. Source lives in `src/native.js` and `scripts/build.mjs`.

Android builds require Android SDK 36 and a compatible JDK/Android Studio. iOS builds require macOS and Xcode 26+. Open `ios/App/App.xcodeproj` and choose your own signing team. The proposed bundle identifier is `ch.subahininadarajh.arraystep`; verify ownership/availability before your first store upload.

## Release state

The web checks and native project generation/sync have passed. Android APK/AAB compilation, iOS compilation, real-device tests, signing, TestFlight and Google Play publication have **not** been completed. No store release is claimed.

The included manually dispatchable GitHub workflow prepares Android debug/unsigned release outputs and an unsigned iOS simulator build. It has not yet run. A simulator build cannot be installed on a physical iPhone. Production publishing requires your own verified developer accounts, signing and store review.

See `release/RELEASE.md` for exact blockers and `release/CONTENT_REVIEW.md` for the content inventory. No paid course, scraped problem statement, EEG data, personal dataset or third-party logo is included. Optional external practice links are not an endorsement.

## Privacy and licensing

Progress and notes remain on the device; export/import moves a user-selected JSON backup. There are no ads, analytics, live AI calls or publisher-operated accounts. The private Sites web host has its own sign-in/hosting infrastructure. See `dist/privacy.html` (release draft) and `THIRD_PARTY_NOTICES.txt`.

Project-specific source/content is reserved for Subahini Nadarajh; no general open-source redistribution license is granted. Third-party components retain their own licenses. `package-lock.json` fixes dependency versions.

## Historical scripts

`make.py`, `expand.py`, and `redesign.py` record earlier construction steps. Do not rerun them against the current app: they are not the supported build process and may overwrite current content. `verify.py` contains additional checks for the original array algorithms. Use `npm run check` and `npm run build` for maintained checks/builds.
