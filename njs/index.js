const { shell, dialog, BrowserWindow, app } = require('electron');

const path = require('node:path')
const utilsMin = require('./util.min');
const { exit } = require('node:process');

//console.log("Hello.")

function createWindow () {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: false,
      nodeIntegration: true
    },
    fullscreen: true,
    minimizable: false,
    darkTheme: true
  })

  win.loadFile('files/index.html')
}

app.whenReady().then(() => {
  if (utilsMin.isCurrentUserRoot() == true) {
    console.log("User is root.")
    dialog.showErrorBox('Did you mean to run as root?', 'This script doesn\'t require or allow its processes to be run as root.\nRun as your default user (not root) and try again.\n\nNote: things break when running applications with root permissions.');
    exit(0);
  }

  createWindow()

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow()
    }
  })
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})