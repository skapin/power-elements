<template>
  <v-ons-page>
    <navbar enabled="false" navType="menu"></navbar>
    <div class="admin-page" v-if="options">
      <apexchart class="chart-display" type="line" :options="globalOptions" :series="globalSeries"></apexchart>

      <!-- <div v-for="stat in stats" v-bind:key="stat.index">
        <hr />
        <apexchart
          class="chart-display"
          type="line"
          :options="options[stat.index]"
          :series="series[stat.index]"
        ></apexchart>
      </div> -->
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
      globalOptions: {},
      globalSeries: []
    };
  },
  methods: {
    getStats() {
      server.getStats().then(result => {
        this.stats = result

        this.globalOptions = {
          legend: {
            show: true,
            showForSingleSeries: true
          },
          chart: {
            id: "global",
            toolbar: {
              show: true
            }
          },
          xaxis: {
            categories: result.flatMap(el =>
              el.results.map(cat => cat.created_at.substring(5, 10))
            )
          }
        };

        result.map(el =>
          this.globalSeries.push({
            name: el.question_name,
            data: el.results.map(item => item.value)
          })
        );

        // result.data.map(el =>
        //   this.globalSeries.push({
        //     name: el.question_name,
        //     data: el.results.map(item => ({
        //       x: item.username,
        //       y: item.value
        //     }))
        //   })
        // );

        result.forEach(element => {
          this.options.push({
            legend: {
              show: true,
              showForSingleSeries: true
            },
            chart: {
              id: element.question_name,
              toolbar: {
                show: true
              }
            },
            xaxis: {
              categories: element.results.map(el =>
                el.created_at.substring(5, 10)
              )
            },
            colors: ["#60C2F6", "#5FAE58"]
          });

          this.series.push([
            {
              name: element.question_name,
              data: element.results.map(item => item.value)
            }
          ]);
        });
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
