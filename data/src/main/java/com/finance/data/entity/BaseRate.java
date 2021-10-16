package com.finance.data.entity;

import lombok.*;

import javax.persistence.*;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;
import java.sql.Timestamp;
import java.util.Date;

@Entity @Table(name = "base_rate")
@NoArgsConstructor @AllArgsConstructor @Builder
@Setter @Getter @ToString
public class BaseRate {
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    @Column(name = "base_rate_seq")
    private long baseRateSeq;

    @NotBlank
    @Size(min = 2, max = 2)
    @Column(name = "country_code")
    private String countryCode;

    @NotNull
    @Column(name = "rate")
    private double rate;

    @Column(name = "standard_date")
    private Date standardDate;

    @Column(name = "update_date")
    private Date updateDate;

    @NotNull
    @Transient
    private long timestamp;
}
