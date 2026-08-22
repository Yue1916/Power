/* 家务打卡 Service Worker —— 离线可用
   更新工具后，把下面的版本号 +1（如 hw-v2），用户下次联网打开即会自动更新缓存。*/
const CACHE = 'hw-v1';
const CORE = ['./', './index.html', './manifest.json', './icon-512.png', './apple-touch-icon.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(CORE)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return; // 只处理同源资源

  const isPage = req.mode === 'navigate' || url.pathname.endsWith('/') || url.pathname.endsWith('index.html');
  if (isPage) {
    // 页面：网络优先，拿到就更新缓存；离线时回退到缓存
    e.respondWith(
      fetch(req).then(res => {
        const cp = res.clone();
        caches.open(CACHE).then(c => c.put('./index.html', cp));
        return res;
      }).catch(() => caches.match('./index.html'))
    );
  } else {
    // 其它静态资源：缓存优先，缺失再联网并回填
    e.respondWith(
      caches.match(req).then(r => r || fetch(req).then(res => {
        const cp = res.clone();
        caches.open(CACHE).then(c => c.put(req, cp));
        return res;
      }))
    );
  }
});
