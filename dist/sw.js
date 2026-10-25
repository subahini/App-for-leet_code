// Cache same-origin study assets only; never cache private authentication responses.
const cacheName='arraystep-assets-v1';const assets=['style.css','app.js','lessons.json','icon.svg','manifest.json'];
self.addEventListener('install',e=>{self.skipWaiting()});
self.addEventListener('activate',e=>e.waitUntil(self.clients.claim()));
self.addEventListener('fetch',e=>{let u=new URL(e.request.url);if(u.origin!==location.origin||!assets.some(a=>u.pathname.endsWith('/'+a)))return;e.respondWith(fetch(e.request).then(r=>{if(r.ok&&!r.redirected){let copy=r.clone();caches.open(cacheName).then(c=>c.put(e.request,copy))}return r}).catch(()=>caches.match(e.request)))});
