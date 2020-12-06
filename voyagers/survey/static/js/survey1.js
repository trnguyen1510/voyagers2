const slidePage = document.querySelector(".slide-page");
const nextBtnFirst = document.querySelector(".firstNext");
const prevBtnSec = document.querySelector(".prev-1");
const nextBtnSec = document.querySelector(".next-1");
const prevBtnThird = document.querySelector(".prev-2");
const nextBtnThird = document.querySelector(".next-2");
const prevBtnFourth = document.querySelector(".prev-3");
const submitBtn = document.querySelector(".submit");
const progressText = document.querySelectorAll(".step p");
const progressCheck = document.querySelectorAll(".step .check");
const bullet = document.querySelectorAll(".step .bullet");
let current = 1;

nextBtnFirst.addEventListener("click", function (event) {
    event.preventDefault();
    slidePage.style.marginLeft = "-25%";
    bullet[current - 1].classList.add("active");
    progressCheck[current - 1].classList.add("active");
    progressText[current - 1].classList.add("active");
    current += 1;
});
nextBtnSec.addEventListener("click", function (event) {
    event.preventDefault();
    slidePage.style.marginLeft = "-50%";
    bullet[current - 1].classList.add("active");
    progressCheck[current - 1].classList.add("active");
    progressText[current - 1].classList.add("active");
    current += 1;
});
nextBtnThird.addEventListener("click", function (event) {
    event.preventDefault();
    slidePage.style.marginLeft = "-75%";
    bullet[current - 1].classList.add("active");
    progressCheck[current - 1].classList.add("active");
    progressText[current - 1].classList.add("active");
    current += 1;
});
submitBtn.addEventListener("click", function () {
    bullet[current - 1].classList.add("active");
    progressCheck[current - 1].classList.add("active");
    progressText[current - 1].classList.add("active");
    current += 1;
    setTimeout(function () {
        alert("Your Form Successfully Signed up");
        location.reload();
    }, 800);
});

prevBtnSec.addEventListener("click", function (event) {
    event.preventDefault();
    slidePage.style.marginLeft = "0%";
    bullet[current - 2].classList.remove("active");
    progressCheck[current - 2].classList.remove("active");
    progressText[current - 2].classList.remove("active");
    current -= 1;
});
prevBtnThird.addEventListener("click", function (event) {
    event.preventDefault();
    slidePage.style.marginLeft = "-25%";
    bullet[current - 2].classList.remove("active");
    progressCheck[current - 2].classList.remove("active");
    progressText[current - 2].classList.remove("active");
    current -= 1;
});
prevBtnFourth.addEventListener("click", function (event) {
    event.preventDefault();
    slidePage.style.marginLeft = "-50%";
    bullet[current - 2].classList.remove("active");
    progressCheck[current - 2].classList.remove("active");
    progressText[current - 2].classList.remove("active");
    current -= 1;
});


// DropDown function
var myData = [
    [
        "United States of America",
        "New York",
        "New York 3-day Adventure. Explore the City!",
        "2021-05-10"
    ],
    [
        "United States of America",
        "San Diego",
        "San Diego. Explore the most popular attractions in the city!",
        "2021-01-16"
    ],
    ["China", "Beijing", "Discover Beijing!", "2021-04-07"],
    ["China", "Shanghai", "Exploring Shanghai", "2021-04-08"],
    ["France", "Paris", "Walk through the Streets of Paris!", "2021-03-31"],
    ["France", "Bordeaux", "Exploring Bordeaux", "2021-03-31"],
    ["England", "London", "Discover London!", "2021-04-04"],
    [
        "Singapore",
        "Singapore",
        "Amazing 3-day Adventure at Singapore!",
        "2021-04-05"
    ],
    [
        "United Arab Emirates",
        "Dubai",
        "Relish in the luxurious sands of Dubai!",
        "2021-07-20"
    ],
    [
        "Thailand",
        "Bangkok",
        "Experience local cultural and heritage",
        "2021-03-05"
    ]
];

function makeDropDown(data, filtersAsArray, targetElement) {
    const filteredArray = filterArray(data, filtersAsArray);

    const uniqueList = getUniqueValues(filteredArray, filtersAsArray.length);

    populateDropDown(targetElement, uniqueList);
}

function applyDropDown() {
    const selectLevel1Value = document.getElementById("level1").value;
    const selectLevel2 = document.getElementById("level2");
    makeDropDown(myData, [selectLevel1Value], selectLevel2);
    applyDropDown2();
}

function applyDropDown2() {
    const selectLevel1Value = document.getElementById("level1").value;
    const selectLevel2Value = document.getElementById("level2").value;
    const selectLevel3 = document.getElementById("level3");
    makeDropDown(myData, [selectLevel1Value, selectLevel2Value], selectLevel3);
}

function applyDropDown3() {
    const selectLevel1Value = document.getElementById("level1").value;
    const selectLevel2Value = document.getElementById("level2").value;
    const selectLevel3Value = document.getElementById("level3").value;
    const selectLevel4 = document.getElementById("level4");
    makeDropDown(myData, [selectLevel1Value, selectLevel2Value, selectLevel3Value], selectLevel4);
}

function afterDocumentLoads() {
    populateFirstLevelDropDown();
    applyDropDown();
    applyDropDown2();
    applyDropDown3();

}

function getUniqueValues(data, index) {
    const uniqueOptions = new Set();
    data.forEach((r) => uniqueOptions.add(r[index]));
    return [...uniqueOptions];
}

function populateFirstLevelDropDown() {
    const uniqueList = getUniqueValues(myData, 0);
    const el = document.getElementById("level1");
    populateDropDown(el, uniqueList);
}

function populateDropDown(el, listArray) {
    el.innerHTML = "";

    listArray.forEach(item => {
        const option = document.createElement("option");
        option.textContent = item;
        el.appendChild(option);
    })
}

function filterArray(data, filtersAsArray) {
    return data.filter(r => filtersAsArray.every((item, i) => item === r[i]));
}

document.getElementById("level1").addEventListener("change", applyDropDown);
document.getElementById("level2").addEventListener("change", applyDropDown2);
document.getElementById("level3").addEventListener("change", applyDropDown3);
document.addEventListener("DOMContentLoaded", afterDocumentLoads);
