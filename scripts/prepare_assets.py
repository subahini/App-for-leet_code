from pathlib import Path
import io, json, plistlib, html
from PIL import Image, ImageDraw

root=Path('.')
svg=Path('dist/icon.svg').read_bytes()
# Existing project-native vector icon; no downloaded artwork.
icon=Image.new('RGB',(1024,1024),'#203d30')
draw=ImageDraw.Draw(icon)
for x,y,w,h in [(95,135,80,240),(215,195,80,180),(335,95,80,280)]:
 draw.rounded_rectangle((x*2,y*2,(x+w)*2,(y+h)*2),radius=32,fill='#cde4bd')
icon.save('ios/App/App/Assets.xcassets/AppIcon.appiconset/AppIcon-512@2x.png')
icon.resize((512,512)).save('release/play-icon.png')
icon.save('release/apple-icon.png')
for d in Path('android/app/src/main/res').glob('mipmap-*'):
 if d.name=='mipmap-anydpi-v26':continue
 scale={'mdpi':1,'hdpi':1.5,'xhdpi':2,'xxhdpi':3,'xxxhdpi':4}[d.name.split('-')[1]]
 for name,size in [('ic_launcher',48),('ic_launcher_round',48),('ic_launcher_foreground',108)]:
  if name.endswith('foreground'):
   target=Image.new('RGBA',(int(size*scale),int(size*scale)),(0,0,0,0));im=icon.resize((int(58*scale),int(58*scale))).convert('RGBA');target.paste(im,((target.width-im.width)//2,(target.height-im.height)//2))
  else:target=icon.resize((int(size*scale),int(size*scale)))
  target.save(d/(name+'.png'))
for f in list(Path('android/app/src/main/res').glob('drawable*/splash.png'))+list(Path('ios/App/App/Assets.xcassets/Splash.imageset').glob('*.png')):
 old=Image.open(f);im=Image.new('RGB',old.size,'#f6f7f3');small=icon.resize((min(180,im.width//3),)*2);im.paste(small,((im.width-small.width)//2,(im.height-small.height)//2));im.save(f,optimize=True)
p=Path('android/app/src/main/res/values/ic_launcher_background.xml');p.write_text(p.read_text().replace('#FFFFFF','#203d30'))
# Retain all bundled package license texts, including the filesystem plugin's transitive native dependency.
licenses=[]
for d in sorted(Path('node_modules/@capacitor').iterdir()):
 if d.name=='cli':continue
 f=next((f for f in d.glob('LICENSE*') if f.is_file()),None)
 meta=json.loads((d/'package.json').read_text())
 if f:licenses.append(meta['name']+' '+meta['version']+'\n'+f.read_text())
text='ArrayStep third-party notices\n\n'+'\n\n'.join(licenses)
Path('THIRD_PARTY_NOTICES.txt').write_text(text)
p=Path('dist/notices.html');s=p.read_text();start=s.index('<pre id="licenses">');end=s.index('</pre>',start)+len('</pre>');p.write_text(s[:start]+'<pre id="licenses">'+html.escape(text)+'</pre>'+s[end:])
privacy={'NSPrivacyTracking':False,'NSPrivacyTrackingDomains':[],'NSPrivacyCollectedDataTypes':[],'NSPrivacyAccessedAPITypes':[{'NSPrivacyAccessedAPIType':'NSPrivacyAccessedAPICategoryFileTimestamp','NSPrivacyAccessedAPITypeReasons':['C617.1']}]}
Path('ios/App/App/PrivacyInfo.xcprivacy').write_bytes(plistlib.dumps(privacy))
p=Path('ios/App/App.xcodeproj/project.pbxproj');s=p.read_text();buildid='A11A57E00000000000000001';fileid='A11A57E00000000000000002'
if fileid not in s:
 s=s.replace('/* Begin PBXBuildFile section */','/* Begin PBXBuildFile section */\n\t\t'+buildid+' /* PrivacyInfo.xcprivacy in Resources */ = {isa = PBXBuildFile; fileRef = '+fileid+' /* PrivacyInfo.xcprivacy */; };')
 s=s.replace('/* Begin PBXFileReference section */','/* Begin PBXFileReference section */\n\t\t'+fileid+' /* PrivacyInfo.xcprivacy */ = {isa = PBXFileReference; lastKnownFileType = text.xml; path = PrivacyInfo.xcprivacy; sourceTree = "<group>"; };')
 s=s.replace('504EC3131FED79650016851F /* Info.plist */,','504EC3131FED79650016851F /* Info.plist */,\n\t\t\t\t'+fileid+' /* PrivacyInfo.xcprivacy */,')
 s=s.replace('files = (\n\t\t\t\t504EC3121FED79650016851F', 'files = (\n\t\t\t\t'+buildid+' /* PrivacyInfo.xcprivacy in Resources */,\n\t\t\t\t504EC3121FED79650016851F')
 p.write_text(s)
print('Original icons and splash screens rendered; dependency notices and iOS file-timestamp privacy declaration included.')
