async function downloadYouTubeVideo(){
	let data= document.getElementById("data").value
    document.getElementById("download").value="Downloading...";
    await eel.start_downloader_thread(data)()

    setTimeout(function(){
        document.getElementById("data").value = "";
        document.getElementById("download").value="Download";
    }, 1000);

}