console.log('enter vue');
new Vue({
 el: "#main",
 delimiters: ['[[', ']]'],
 data: {
   projects: [],
   testing: 'TESTING',
  },
  methods: {
    getProjects: function() {
    let that = this;
    this.$http.get("/api/project/")
      .then((response) => {
        that.projects = response.data.objects;
        console.log('getProjects success');
        console.log(this.projects);
      })
      .catch((err) => {
        console.log('getProjects error');
        console.log(err);
      })
    },
  },
  mounted: function() {
    this.getProjects();
    console.log('mounted');
  },
});
