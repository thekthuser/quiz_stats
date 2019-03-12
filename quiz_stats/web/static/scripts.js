new Vue({
 el: "#main",
 delimiters: ['[[', ']]'],
 data: {
   questions: [],
  },
  methods: {
    getProjects: function() {
    this.$http.get("/api/project/")
      .then((response) => {
        this.projects = response.data.objects;
      })
      .catch((err) => {
        console.log(err);
      })
    },
    getQuestions: function() {
    this.$http.get("/api/question/")
      .then((response) => {
        this.questions = response.data.objects;
        console.log(this.questions);
      })
      .catch((err) => {
        console.log(err);
      })
    },
  },
  mounted: function() {
    this.getQuestions();
  },
});
