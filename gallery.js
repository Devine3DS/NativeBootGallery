"use strict";
const cards = [...document.querySelectorAll(".card")];
const search = document.getElementById("search");
const group = document.getElementById("group");
const filters = [...document.querySelectorAll(".filter")];
const dialog = document.getElementById("preview-dialog");
const video = document.getElementById("full-video");
const still = document.getElementById("full-image");
const note = document.getElementById("preview-note");
let filter = "all";
function update() {
  const query = search.value.trim().toLowerCase();
  let count = 0;
  for (const card of cards) {
    card.hidden = (filter !== "all" && card.dataset.kind !== filter)
      || (group.value !== "all" && card.dataset.group !== group.value)
      || !card.dataset.search.includes(query);
    if (!card.hidden) count++;
  }
  document.getElementById("results").textContent = `${count} of ${cards.length} animations`;
  document.getElementById("empty").hidden = count > 0;
  for (const section of document.querySelectorAll("[data-section-kind]")) {
    const visible = cards.filter(card => card.dataset.kind === section.dataset.sectionKind && !card.hidden).length;
    section.hidden = visible === 0;
    section.querySelector(".section-count").textContent = `${visible} animations`;
  }
  for (const option of group.options) {
    option.hidden = filter !== "all" && option.value !== "all" && option.dataset.kind !== filter;
  }
}
for (const button of filters) button.addEventListener("click", () => {
  filter = button.dataset.filter;
  // Switching type should not leave the new tab hidden by a previous group.
  group.value = "all";
  for (const candidate of filters) {
    const active = candidate === button;
    candidate.classList.toggle("active", active);
    candidate.setAttribute("aria-pressed", String(active));
  }
  update();
});
search.addEventListener("input", update);
for (const link of document.querySelectorAll(".category-links a")) link.addEventListener("click", () => {
  search.value = "";
  const kind = link.getAttribute("href") === "#custom-animations" ? "custom" : "original";
  filters.find(button => button.dataset.filter === kind).click();
});
group.addEventListener("change", update);
document.getElementById("clear").addEventListener("click", () => {
  search.value = ""; group.value = "all"; filters[0].click(); search.focus();
});
for (const button of document.querySelectorAll("[data-image]")) button.addEventListener("click", () => {
  document.getElementById("preview-title").textContent = button.dataset.title;
  const motion = Boolean(button.dataset.preview);
  still.hidden = motion; video.hidden = !motion;
  if (motion) {
    video.src = button.dataset.preview;
    video.poster = button.dataset.image;
    video.load();
    note.textContent = `Native-renderer recording with ${button.dataset.sound} sound. Press Play to watch and listen. Xbox hardware may render some details differently.`;
  } else {
    still.src = button.dataset.image;
    still.alt = `${button.dataset.title}: fully revealed emblem and XBOX 360 lettering`;
    note.textContent = "Captured from the actual exported animation at 5.8 seconds, with the emblem and lettering fully visible.";
  }
  document.body.classList.add("modal-open");
  dialog.showModal();
});
document.getElementById("close-preview").addEventListener("click", () => dialog.close());
dialog.addEventListener("click", event => {
  if (event.target !== dialog) return;
  const r = dialog.getBoundingClientRect();
  if (event.clientX < r.left || event.clientX > r.right || event.clientY < r.top || event.clientY > r.bottom) dialog.close();
});
dialog.addEventListener("close", () => {
  video.pause(); video.removeAttribute("src"); video.load();
  document.body.classList.remove("modal-open");
});
update();
