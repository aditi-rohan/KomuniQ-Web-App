function deleteMessage(messageID) {
  fetch("/delete-message", {method: "POST", body: JSON.stringify({messageID: messageID}), }).then((_res) => {window.location.href = "/"});
}