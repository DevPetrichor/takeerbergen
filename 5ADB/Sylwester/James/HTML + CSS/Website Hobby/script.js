// Helper: extract only the <main class="content">...</main> part
function extractContent(html) {
  const parser = new DOMParser();
  const doc = parser.parseFromString(html, "text/html");
  const content = doc.querySelector(".content");
  return content ? content.innerText.toLowerCase() : "";
}



// LIVE SEARCH ACROSS ALL PAGES
async function liveSearch() {
  const query = document.getElementById("searchInput").value.toLowerCase();
  const resultsBox = document.getElementById("liveResults");

  if (!query) {
    resultsBox.style.display = "none";
    resultsBox.innerHTML = "";
    return;
  }

  const pages = [
    "index.html",
    "simracing.html",
    "computers.html",
    "tekenen.html",
    "voetbal.html",
    "muziek.html"
  ];

  let matches = [];

  for (const page of pages) {
    const response = await fetch(page);
    const html = await response.text();
    const text = extractContent(html);

    if (text.includes(query)) {
      matches.push(page);
    }
  }

  resultsBox.style.display = "block";
  resultsBox.innerHTML = "";

  if (matches.length === 0) {
    resultsBox.innerHTML = "<div>Geen resultaten</div>";
    return;
  }

  matches.forEach(page => {
    const item = document.createElement("div");
    item.textContent = page.replace(".html", "");
    item.onclick = () => {
      window.location.href = page + "?search=" + query;
    };
    resultsBox.appendChild(item);
  });
}



// BUTTON SEARCH (OPTIONAL)
async function searchAllPages() {
  const query = document.getElementById("searchInput").value.toLowerCase();
  if (!query) return;

  const pages = [
    "index.html",
    "simracing.html",
    "computers.html",
    "tekenen.html",
    "voetbal.html",
    "muziek.html"
  ];

  let results = [];

  for (const page of pages) {
    const response = await fetch(page);
    const html = await response.text();
    const text = extractContent(html);

    if (text.includes(query)) {
      results.push(page);
    }
  }

  if (results.length === 0) {
    alert("Geen resultaten gevonden");
    return;
  }

  if (results.length === 1) {
    window.location.href = results[0] + "?search=" + query;
  } else {
    alert("Gevonden in:\n\n" + results.join("\n"));
  }
}



// AUTO‑HIGHLIGHT + SCROLL WHEN OPENING A PAGE
window.onload = function () {
  const params = new URLSearchParams(window.location.search);
  const search = params.get("search");
  if (!search) return;

  const content = document.querySelector(".content");
  if (!content) return;

  // Remove old highlights
  content.innerHTML = content.innerHTML.replace(/<mark class="highlight">|<\/mark>/g, "");

  const text = content.innerHTML;
  const lower = text.toLowerCase();
  const query = search.toLowerCase();

  let index = lower.indexOf(query);
  if (index === -1) return;

  // Highlight ALL matches
  let newHTML = "";
  let lastIndex = 0;

  while (index !== -1) {
    newHTML += text.substring(lastIndex, index)
      + `<mark class="highlight">${text.substring(index, index + query.length)}</mark>`;
    lastIndex = index + query.length;
    index = lower.indexOf(query, lastIndex);
  }

  newHTML += text.substring(lastIndex);
  content.innerHTML = newHTML;

  // Scroll to first match
  const firstMatch = document.querySelector("mark.highlight");
  if (firstMatch) {
    firstMatch.scrollIntoView({
      behavior: "smooth",
      block: "center"
    });
  }
};