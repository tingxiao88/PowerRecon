let peerConnection;
const config = {
  iceServers: [
    {
      urls: "stun:stun.l.google.com:19302",
    },
    // {
    //   "urls": "turn:TURN_IP?transport=tcp",
    //   "username": "TURN_USERNAME",
    //   "credential": "TURN_CREDENTIALS"
    // }
  ],
};

const socket = io.connect(window.location.origin);
const video = document.querySelector("video");

currentTemp = document.querySelector("#currentTemperature");
optimumTemp = document.querySelector("#optimunTemp");
AirconTemp = document.querySelector("#AirconTemperature");
currentFan = document.querySelector("#currentFanSpeed");
person = document.querySelector("#Person");
current_time = document.querySelector("#current_time");
well_cooled = document.querySelector("#well_cooled");
well_cooled.innerHTML = "No, the room temp is not optimun";
well_cooled.style.color = "#a4161a";

console.log(currentTemp.innerHTML);
console.log(optimumTemp);
console.log(AirconTemp);
console.log(currentFan);

socket.on("send", (file) => {
  console.log("data_incomming");
  currentTemp.innerHTML = file["current-temp"];
  optimumTemp.innerHTML = file["optimun_temp"];
  currentFan.innerHTML = file["aircon-fan"];
  AirconTemp.innerHTML = file["aircon-temp"];
  person.innerHTML = file["person"];
  current_time.innerHTML = file["time"].slice(0, -7);

  if (file["well_cooled"] == "true") {
    well_cooled.innerHTML = "Yes, the room is well cooled!";
    well_cooled.style.color = "#2b9348";
  } else {
    well_cooled.innerHTML = "No, the room temp is not optimun";
    well_cooled.style.color = "#a4161a";
  }
  if (file["aircon-temp"] == "OFF" && file["aircon-fan"] == "OFF") {
    AirconTemp.style.color = "#a4161a";
    currentFan.style.color = "#a4161a";
  } else {
    AirconTemp.style.color = "white";
    currentFan.style.color = "white";
  }
});

// socket.on("send", (file) => {
//   console.log("data_incomming");
//   console.log(file);
// });

socket.on("offer", (id, description) => {
  console.log("offer");
  peerConnection = new RTCPeerConnection(config);
  peerConnection
    .setRemoteDescription(description)
    .then(() => peerConnection.createAnswer())
    .then((sdp) => peerConnection.setLocalDescription(sdp))
    .then(() => {
      socket.emit("answer", id, peerConnection.localDescription);
    });
  peerConnection.ontrack = (event) => {
    video.srcObject = event.streams[0];
  };
  peerConnection.onicecandidate = (event) => {
    if (event.candidate) {
      socket.emit("candidate", id, event.candidate);
    }
  };
});

socket.on("candidate", (id, candidate) => {
  peerConnection
    .addIceCandidate(new RTCIceCandidate(candidate))
    .catch((e) => console.error(e));
});

socket.on("connect", () => {
  socket.emit("watcher");
});

socket.on("broadcaster", () => {
  socket.emit("watcher");
});

window.onunload = window.onbeforeunload = () => {
  socket.close();
  peerConnection.close();
};
