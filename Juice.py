import wx
import os
import wget
import threading

class MinecraftServerDownloader(wx.Frame):
    def __init__(self, parent, title):
        super(MinecraftServerDownloader, self).__init__(parent, title=title, size=(400, 200))
        
        self.panel = wx.Panel(self)
        
        self.url_label = wx.StaticText(self.panel, label="下载链接:")
        self.url_text = wx.TextCtrl(self.panel)
        
        self.version_label = wx.StaticText(self.panel, label="版本号:")
        self.version_text = wx.TextCtrl(self.panel)
        
        self.start_button = wx.Button(self.panel, label="启动服务器")
        self.start_button.Bind(wx.EVT_BUTTON, self.on_start_button_clicked)
        
        self.download_button = wx.Button(self.panel, label="下载服务器")
        self.download_button.Bind(wx.EVT_BUTTON, self.on_download_button_clicked)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.url_label, 0, wx.ALL, 5)
        sizer.Add(self.url_text, 0, wx.EXPAND|wx.ALL, 5)
        sizer.Add(self.version_label, 0, wx.ALL, 5)
        sizer.Add(self.version_text, 0, wx.EXPAND|wx.ALL, 5)
        sizer.Add(self.start_button, 0, wx.ALL, 5)
        sizer.Add(self.download_button, 0, wx.ALL, 5)

        self.panel.SetSizer(sizer)
        self.Show()

    def on_start_button_clicked(self, event):
        version = self.version_text.GetValue()
        server_path = f"./servers/{version}/server.jar"
        if os.path.exists(server_path):
            print("启动服务器:", server_path)
            # 在这里编写启动服务器的代码
        else:
            print("未找到服务器文件，请先下载服务器")

    def on_download_button_clicked(self, event):
        url = self.url_text.GetValue()
        version = self.version_text.GetValue()
        download_thread = threading.Thread(target=self.download_server, args=(url, version))
        download_thread.start()

    def download_server(self, url, version):
        server_path = f"./servers/{version}"
        os.makedirs(server_path, exist_ok=True)
        file_path = f"{server_path}/server.jar"
        print("开始下载:", url)
        wget.download(url, out=file_path)
        print("\n下载完成:", file_path)

if __name__ == '__main__':
    app = wx.App()
    MinecraftServerDownloader(None, title='Minecraft Server Downloader')
    app.MainLoop()import wx
import os
import wget
import threading

class MinecraftServerDownloader(wx.Frame):
    def __init__(self, parent, title):
        super(MinecraftServerDownloader, self).__init__(parent, title=title, size=(400, 200))
        
        self.panel = wx.Panel(self)
        
        self.url_label = wx.StaticText(self.panel, label="下载链接:")
        self.url_text = wx.TextCtrl(self.panel)
        
        self.version_label = wx.StaticText(self.panel, label="版本号:")
        self.version_text = wx.TextCtrl(self.panel)
        
        self.start_button = wx.Button(self.panel, label="启动服务器")
        self.start_button.Bind(wx.EVT_BUTTON, self.on_start_button_clicked)
        
        self.download_button = wx.Button(self.panel, label="下载服务器")
        self.download_button.Bind(wx.EVT_BUTTON, self.on_download_button_clicked)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.url_label, 0, wx.ALL, 5)
        sizer.Add(self.url_text, 0, wx.EXPAND|wx.ALL, 5)
        sizer.Add(self.version_label, 0, wx.ALL, 5)
        sizer.Add(self.version_text, 0, wx.EXPAND|wx.ALL, 5)
        sizer.Add(self.start_button, 0, wx.ALL, 5)
        sizer.Add(self.download_button, 0, wx.ALL, 5)

        self.panel.SetSizer(sizer)
        self.Show()

    def on_start_button_clicked(self, event):
        version = self.version_text.GetValue()
        server_path = f"./servers/{version}/server.jar"
        if os.path.exists(server_path):
            print("启动服务器:", server_path)
            # 在这里编写启动服务器的代码
        else:
            print("未找到服务器文件，请先下载服务器")

    def on_download_button_clicked(self, event):
        url = self.url_text.GetValue()
        version = self.version_text.GetValue()
        download_thread = threading.Thread(target=self.download_server, args=(url, version))
        download_thread.start()

    def download_server(self, url, version):
        server_path = f"./servers/{version}"
        os.makedirs(server_path, exist_ok=True)
        file_path = f"{server_path}/server.jar"
        print("开始下载:", url)
        wget.download(url, out=file_path)
        print("\n下载完成:", file_path)

if __name__ == '__main__':
    app = wx.App()
    MinecraftServerDownloader(None, title='Minecraft Server Downloader')
    app.MainLoop()
