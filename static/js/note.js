var sidebar = document.getElementById("sidebar");
    document.addEventListener("mousemove", function(event) {
      var xPosition = event.clientX;
      if (xPosition < 50) {
        sidebar.style.left = "0";
      } else if (xPosition > 300) {
        sidebar.style.left = "-300px";
      }
});

document.addEventListener('mouseleave', () => {
  document.getElementById('sidebar').style.left = '-300px';
});

function toggleDropdown() {
  let dropdown = document.getElementById("dropdown");
  if (dropdown.style.display === "none") {
    dropdown.style.display = "block";
    setTimeout(() => {
      let items = document.querySelectorAll(".dropdown-item");
      items.forEach((item, i) => {
        setTimeout(() => {
          item.style.opacity = "1";
          item.style.transform = "translateY(0)";
        }, i * 50);
      });
    }, 0);
  } else {
    let items = document.querySelectorAll(".dropdown-item");
    items.forEach((item, i) => {
      setTimeout(() => {
        item.style.opacity = "0";
        item.style.transform = "translateY(-10px)";
      }, (items.length - i - 1) * 50);
    });
    setTimeout(() => {
      dropdown.style.display = "none";
    }, items.length * 50);
  }
}

const noteTitle = document.querySelector('.noteTitle');
noteTitle.addEventListener('mousedown', () => {
  noteTitle.contentEditable = 'true';
  noteTitle.focus();
});

const noteText = document.querySelector('.noteText');
noteText.addEventListener('mousedown', () => {
  noteText.contentEditable = 'true';
  noteText.focus();
});

document.getElementById('sidebar').addEventListener('mouseover', () => {
  document.querySelector('.content').style.marginLeft = "300px";
});

document.getElementById('sidebar').addEventListener('mouseout', () => {
  document.querySelector('.content').style.marginLeft = "0";
});

function inInput(){
  if (document.getElementById('noteTitle').innerText.length  === 0) {
    document.getElementById('inputTitle').value = "Title";
  }
  else{
    document.getElementById('inputTitle').value = document.getElementById('noteTitle').innerText;
  }
  document.getElementById('inputText').value = document.getElementById('noteText').innerText;
  document.getElementById('inputText').value = document.getElementById('noteText').innerText;
}

document.addEventListener('keydown', function(event) {
  if (event.ctrlKey && event.key === 'z' && document.hasFocus()) {
    event.preventDefault();
    document.execCommand('undo');
  }
});
