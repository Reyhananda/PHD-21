// import Chart from "chart.js/auto";
if (!window.moment) {
  document.write('<script src="assets/plugins/moment/moment.min.js"></script>');
}
const moment = window.moment;

console.log("tess");
const data = [
  { day: "Mon", count: 10 },
  { day: "Tue", count: 20 },
  { day: "Wed", count: 15 },
  { day: "Thu", count: 25 },
  { day: "Fri", count: 22 },
  { day: "Sat", count: 30 },
  { day: "Sun", count: 28 },
];
console.log(document.getElementById("acquisitions"));
new Chart(document.getElementById("acquisitions"), {
  type: "bar",
  data: {
    labels: data.map((row) => row.day),
    datasets: [
      {
        label: "Acquisitions by year",
        data: data.map((row) => row.count),
      },
    ],
  },
});
