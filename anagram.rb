#!/usr/bin/env ruby

ANAGRAM_LENGTH = 2
SET_LENGTH = nil
MINIMUM_WORD_LENGTH = 4
KEY_LENGTH = 1

class Corpus
  def initialize()
    @words = []
  end

  def stdin()
    $stdin.read.gsub(/[\W\d]+/, ' ').downcase.split.each do |word|
      add_word(word)
    end
  end

  def add_word(word)
    return if word.length < MINIMUM_WORD_LENGTH or @words.include?(word)
    @words << word
  end

  def find_matches(anagram_length=ANAGRAM_LENGTH, set_length=SET_LENGTH)
    matches = {}
    data = {}
    match_length = 2
    @words.combination(anagram_length) do |pair|
      composition = pair.join.each_char.to_a.sort.join
      key = composition[0, KEY_LENGTH]
      data[key] = {} unless data[key]
      data[key][composition] = [] unless data[key][composition]
      unique = true
      data[key][composition].each do |existing|
        if existing & pair != []
          unique = false
          break
        end
      end
      if unique
        data[key][composition] << pair
        matches[composition] = data[key][composition].length
        match_length = matches[composition] if matches[composition] > match_length
      end
    end
    unless set_length
      puts "(length is #{match_length})"
    else
      match_length = set_length
    end
    matches.each_pair do |composition,length|
      next if length != match_length
      data[composition[0, KEY_LENGTH]][composition].each do |pair|
        print "#{pair.join(', ')}; "
      end
      puts
    end
  end
end

if __FILE__ == $0
  corpus = Corpus.new
  corpus.stdin()
  corpus.find_matches()
end
