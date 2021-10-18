package com.finance.data.service;

import com.finance.data.entity.Cryptocurrency;
import com.finance.data.repository.CryptocurrencyRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Date;
import java.util.Locale;

@Service
public class CryptocurrencyService {

    @Autowired
    private CryptocurrencyRepository cryptocurrencyRepository;

    public Cryptocurrency saveCryptocurrency(Cryptocurrency cryptocurrency) {
        Cryptocurrency newCryptocurrency = Cryptocurrency.builder()
                .cryptoCode(cryptocurrency.getCryptoCode().toUpperCase(Locale.ROOT))
                .maxPrice(cryptocurrency.getMaxPrice())
                .minPrice(cryptocurrency.getMinPrice())
                .fromData(cryptocurrency.getFromData())
                .standardDate(new Date(cryptocurrency.getTimestamp()*1000L))
                .updateDate(new Date())
                .build();
        return cryptocurrencyRepository.save(newCryptocurrency);
    }
}
