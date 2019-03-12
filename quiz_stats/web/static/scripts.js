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
    sendAnswer: function(project_id, question_id, is_active) {
      console.log('sendAnswer');
      console.log(project_id);
      console.log(question_id);
      console.log(is_active);
    },
  },
  mounted: function() {
    this.getQuestions();
  },
});
