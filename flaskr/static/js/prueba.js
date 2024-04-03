import {Viewer} from "@photo-sphere-viewer/core";

const viewer = new Viewer ({
    container: document.querySelector('#viewer'),
    panorama: '../img/Scene2.jpg',
});

const nodes = [
    { id: 'node-1', panorama: '001.jpg', links: [{ nodeId: 'node-2', position: { textureX: 1500, textureY: 780 } }] },
    { id: 'node-2', panorama: '002.jpg', links: [{ nodeId: 'node-1', position: { textureX: 3000, textureY: 780 } }] },
];
