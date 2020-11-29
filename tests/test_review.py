import unittest
from app.models import Review

class TestReview(unittest.TestCase):

  def setUp(self):
    self.new_review = Review(12345,'Review for movies',"https://image.tmdb.org/t/p/w500/jdjdjdjn",'This movie is the best thing since sliced bread')

  def test_instance(self):
    self.assertTrue(isinstance(self.new_review,Review))


  # def test_check_instance_variables(self):
  #   self.assertEquals(self.new_review.movie_id,12345)
  #   self.assertEquals(self.new_review.movie_title,'Review for movies')
  #   self.assertEquals(self.new_review.image_path,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
  #   self.assertEquals(self.new_review.movie_review,'This movie is the best thing since sliced bread')
  #   self.assertEquals(self.new_review.user,self.user_James)


  # def test_save_review(self):
  #   self.new_review.save_review()
  #   self.assertTrue(len(Review.query.all())>0)


  # def test_get_review_by_id(self):

  #   self.new_review.save_review()
  #   got_reviews = Review.get_reviews(12345)
  #   self.assertTrue(len(got_reviews) == 1)