


  document.querySelector('button').addEventListener('click', () => {
    window.location.reload();
  });

  // Listen to changes in the network state, reload when online.
  // This handles the case when the device is completely offline.
  window.addEventListener('online', () => {
    window.location.reload();
  });

  // Check if the server is responding & reload the page if it is.
  // This handles the case when the device is online, but the server
  // is offline or misbehaving.
  async function checkNetworkAndReload() {
    try {
      const response = await fetch('.');
      // Verify we get a valid response from the server
      if (response.status = 200) {
        return;
      }
      else if(response.status < 500) {
        window.location.reload();
        return;
      };
    } catch {
      // Unable to connect to the server, ignore.
    }
    window.setTimeout(checkNetworkAndReload, 2500);
  }

  checkNetworkAndReload();
