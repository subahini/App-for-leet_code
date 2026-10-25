import { Capacitor } from '@capacitor/core';
import { Browser } from '@capacitor/browser';
import { Filesystem, Directory, Encoding } from '@capacitor/filesystem';
import { Share } from '@capacitor/share';
window.arraystepNative = {
  active: Capacitor.isNativePlatform(),
  async open(url) { await Browser.open({url}); },
  async exportProgress(data) {
    const file = await Filesystem.writeFile({path:'arraystep-progress.json',data:JSON.stringify(data,null,2),directory:Directory.Cache,encoding:Encoding.UTF8});
    await Share.share({title:'ArrayStep progress backup',url:file.uri,dialogTitle:'Save your study progress'});
  }
};
