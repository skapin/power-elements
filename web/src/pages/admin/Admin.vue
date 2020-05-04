<template>
  <v-ons-page>
    <navbar enabled="false" navType="menu"></navbar>
    <div class="admin-page" v-if="globalOptions">
      <apexchart class="chart-display" type="line" :options="globalOptions" :series="globalSeries"></apexchart>
    </div>
  </v-ons-page>
</template>

<script>
import Navbar from "../../components/navbar/Navbar";
import server from "./../../api/server.vue";
import VueApexCharts from "vue-apexcharts";

export default {
  name: "admin",
  components: {
    Navbar,
    apexchart: VueApexCharts
  },
  data() {
    return {
      stats: [],
      options: [],
      series: [],
      reversedResult: [],
      globalOptions: {},
      globalSeries: [],
      falseData: [['2020-05-04', 17], ['2020-05-03', 23], ['2020-05-03', 30], ['2020-05-02', 35], ['2020-05-01', 20], ['2020-04-30', 50], ['2020-04-29', 60], ['2020-04-28', 55], ['2020-04-28', 70], ['2020-04-27', 42]]
    };
  },
  methods: {
    getStats() {
      server.getStats().then(result => {
        this.stats = result;

        this.globalOptions = {
          legend: {
            show: true,
            showForSingleSeries: true
          },
          yaxis: {
            min:0,
            max:100,
          },
          xaxis: {
            type: 'datetime'
          },
          annotations: {
            yaxis: [
              {
                y: 60,
                y2: 100,
                borderColor: "#000",
                fillColor: "#FFCCCB",
                label: {
                  text: "zone à risque"
                }
              }
            ]
          },
          chart: {
            id: "global",
            toolbar: {
              show: true
            }
          },
        };
        // this.reversedResult = result.concat(this.falseData).reverse()
        this.globalSeries.push({
            name: 'score',
            data: this.falseData.reverse().map(item => ({
                x: item[0],
                y: item[1]
            }))
        })
      });
    }
  },
  mounted: function() {
    this.getStats();
  }
};
</script>

<style lang='scss' scoped>
.page-title {
  text-align: center;
}

.btn:hover {
  cursor: pointer;
}
.admin-page {
  max-width: 1200px;
  margin: auto;
}
.chart-display {
  margin: 20px auto;
  height: 200px;
}
</style>
