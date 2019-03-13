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
    sendAnswer: function(project_id, question_id, answer) {
      let data = {'project': project_id, 'question': '/api/question/' + question_id, 'answer': answer}
      this.$http.post('/api/answer/', data, {
      }, 
      headers={'content-type':'application/json'});
    },
  },
  mounted: function() {
    this.getQuestions();
  },
});
